'use strict';

chatApp
.service('ChatSocket', ['$q', '$rootScope', 'WebSocket', function($q, $rootScope, WebSocket) {
    var open = $q.defer();
    var deferred_list = {};

    var service = {
        open: open.promise
    };

    // Generics
    WebSocket.onopen(function() {
        open.resolve(true);
    });

    WebSocket.onmessage(function(message) {
        var json_data = angular.fromJson(message.data);

        if(json_data.type) {
            $rootScope.$broadcast(json_data.type, json_data.data);
        }
    });

    // Subscription
    service.subscribe = function(boardId) {
        var message = {
            'type': 'boards.subscribe',
            'data': {
                'board_id': boardId
            }
        };
        WebSocket.send(angular.toJson(message));
    };

    // Set username
    service.setUserName = function(username) {
        var message = {
            'type': 'user.setname',
            'data': {
                'username': username
            }
        };
        WebSocket.send(angular.toJson(message));
    };

    return service;
}]);
