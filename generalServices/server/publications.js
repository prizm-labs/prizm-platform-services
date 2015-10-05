Meteor.publish('channels', function(){

    return Channels.find();
});

Meteor.publish('appsSub', function(){

    return Apps.find();
});

Meteor.publish('releases', function(){

    return Releases.find();
});
