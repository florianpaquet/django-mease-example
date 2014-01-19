var chatApp = angular.module('ChatApp', ['ngCookies', 'restangular', 'angular-websocket']);

chatApp

// WebSocket
.config(['WebSocketProvider', function(WebSocketProvider) {
    WebSocketProvider
    .prefix('')
    .uri('ws://localhost:9090');
}])

// Restangular
.run(['Restangular', '$cookies', function(Restangular, $cookies) {
    // Root Url
    Restangular.setBaseUrl('/api');

    // CSRF Token
    Restangular.setDefaultHeaders({
        'X-CSRFToken': $cookies.csrftoken,
    });
}]);
