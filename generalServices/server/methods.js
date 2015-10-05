Meteor.methods({

  generatePlaylist: function(desiredSessionLength) { //minutes

    // assuming average game length of 2.5 minutes
    var averageGameLength = 2.5;

    var targetPlaylistGameCount = Math.floor(desiredSessionLength/averageGameLength);

    var gamePool = Apps.find().fetch();
    // should filter apps registry to match number of players,
    // player profile, and group profile

    var playlist = fillPlaylist(gamePool,targetPlaylistGameCount);
  }
});

function fillPlaylist(gamePool, totalGames) {

  return [];
}
