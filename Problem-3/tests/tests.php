<?php
class tests extends \PHPUnit\Framework\TestCase {
    private $baseUrl = 'http://localhost:8080/index.php';
    private $songList = '/review/read';
    private $createUser = '/user/signup';
    private $loginUser = '/user/login';
    private $createSong = '/review/create';
    private $updateSong = '/review/update';
    private $deleteSong = '/review/delete';

    protected $client;

    protected function setUp() : void{
       parent::setUp();
       $this->client = new \GuzzleHttp\Client(["base_uri" => $this->baseUrl]);
    }

    public function testGet_ReviewList() {
        $response = $this->client->get($this->baseUrl . $this->songList);
        $this->assertEquals(200, $response->getStatusCode());
    }

    // If using an username that already exists, test will fail with
    // response code 409.
    public function testPost_CreateUser() {
        $userData = [
            'username' => 'example100',
            'email' => 'example100@gmail.com',
            'password' => 'example100',
        ];
        $response = $this->client->post($this->baseUrl . $this->createUser, [
            'json' => $userData,
        ]);
        $this->assertEquals(201, $response->getStatusCode());
    }

    public function testPost_LoginUser() {
        $userData = [
            'email' => 'example99@gmail.com',
            'password' => 'example99',
        ];
        $response = $this->client->post($this->baseUrl . $this->loginUser, [
            'json' => $userData,
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    // Test login where the username does not exist
    public function testPost_FailedLoginUsername() {
        $userData = [
            'email' => 'example98@gmail.com',
            'password' => 'example99',
        ];
        $response = $this->client->post($this->baseUrl . $this->loginUser, [
            'json' => $userData,
        ]);
        $this->assertEquals(404, $response->getStatusCode());
    }

    // Test login where the password is incorrect
    public function testPost_FailedLoginPassword() {
        $userData = [
            'email' => 'example99@gmail.com',
            'password' => 'example98',
        ];
        $response = $this->client->post($this->baseUrl . $this->loginUser, [
            'json' => $userData,
        ]);
        $this->assertEquals(401, $response->getStatusCode());
    }

    public function testPost_NewSong() {
        $songData = [
            'username' => 'example99',
            'artist' => 'Calum Scott',
            'song' => 'Heaven',
            'rating' => 5,
        ];
        $response = $this->client->post($this->baseUrl . $this->createSong, [
            'json' => $songData,
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testPut_UpdateSong() {
        $songData = [
            'id' => '5',
            'rating' => 1,
        ];
        $response = $this->client->put($this->baseUrl . $this->updateSong, [
            'json' => $songData,
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testDelete_DeleteSong() {
        $songData = [
            'id' => '4',
            'username' => 'ryan',
            'song' => 'Seven',
            'artist' => 'Jung Kook',
        ];
        $response = $this->client->delete($this->baseUrl . $this->deleteSong, [
            'json' => $songData,
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function tearDown() : void{
        parent::tearDown();
        $this->client = null;
     }
}
?>