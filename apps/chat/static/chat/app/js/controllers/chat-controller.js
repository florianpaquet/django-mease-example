'use strict';

chatApp
.controller('ChatController', ['$scope', '$rootScope', '$timeout', 'ChatSocket', 'Restangular', 'urls', function($scope, $rootScope, $timeout, ChatSocket, Restangular, urls) {

    var baseBoards = Restangular.all('boards');
    var baseMessages = Restangular.all('messages');


    // Me

    $scope.me = {
        username: ""
    };

    var baseUserForm = {
        username: "",
    };

    function resetUserForm() {
        $scope.userForm = angular.copy(baseUserForm);
    }

    $scope.changeUserName = function(username) {
        if(username) {
            $scope.me.username = username;
            resetUserForm();
            ChatSocket.setUserName(username);
        }
    };

    $rootScope.$on('me.setname', function(e, username) {
        $scope.me.username = username;
    });


    // Users

    $scope.users = [];

    $rootScope.$on('user.onboard', function(e, users) {
        $scope.users.push.apply($scope.users, users);
    });

    $rootScope.$on('user.joinboard', function(e, user) {
        $scope.users.push(user);
    });

    $rootScope.$on('user.leaveboard', function(e, userId) {
        _.remove($scope.users, function(user) { return user.id == userId; });
    });

    $rootScope.$on('user.setname', function(e, newUser) {
        var user = _.find($scope.users, function(u) { return u.id == newUser.id; });
        user.username = newUser.username;
    });


    // Boards

    $scope.board = null;

    var baseBoardForm = {
        name: ""
    };

    baseBoards.getList().then(
        function(boards) {
            $scope.boards = boards;
        }
    );

    function resetBoardForm() {
        $scope.boardForm = angular.copy(baseBoardForm);
    }

    $scope.createBoard = function(name) {
        baseBoards.post({name: name}).then(
            function(board) {
                resetBoardForm();
                $scope.subscribeToBoard(board);
            }
        );
    };

    $scope.subscribeToBoard = function(board) {
        $scope.users = [];
        $scope.messages = [];
        $scope.board = board;

        baseMessages.one(board.id).getList().then(
            function(messages) {
                $scope.messages = messages;
                ChatSocket.subscribe($scope.board.id);

                $timeout(function() {
                    $('#new-message input').focus();
                }, 0);
            }
        )
    };

    $rootScope.$on('boards.created', function(e, board) {
        $scope.boards.push(board);
    });


    // Messages


    $scope.messages = [];

    var messagesList = $('#messages-list');

    var baseMessageForm = {
        content: ""
    };

    function resetMessageForm() {
        $scope.messageForm = angular.copy(baseMessageForm);
    }

    function scrollBottomMessages() {
        var force = force || true;
        var newScrollHeight = messagesList.prop('scrollHeight');

        messagesList.scrollTop(newScrollHeight);
    }

    $scope.sendMessage = function(content) {
        var message = {
            board: $scope.board.id,
            username: $scope.me.username,
            content: content,
        };

        baseMessages.post(message).then(
            function() {
                resetMessageForm();
            }
        );
    };

    $rootScope.$on('messages.created', function(e, message) {
        $scope.messages.push(message);
    });

    $scope.$watch('messages', function(newMessages, oldMessages) {
        var scrollPosition = messagesList.prop('scrollTop') + messagesList.height();
        var scrollHeight = messagesList.prop('scrollHeight');

        if(scrollHeight - scrollPosition <= 10 || oldMessages.length == 0) {
            $timeout(scrollBottomMessages, 0);
        }
    }, true);


}]);
