Apps = new Meteor.Collection("apps");
Channels = new Meteor.Collection("channels");
Releases = new Meteor.Collection("releases");

Products = new Meteor.Collection("products"); // market
Users = new Meteor.Collection("users"); // tabletop
Purchases = new Meteor.Collection("purchases"); // library

var pc = [
  {
    "product_name":"Plants Vs. Zombies",
    "user_first_name":"Jimmy"
  }
]

var u = [
  {
    "first_name":"Michael",
    "avatar":"image.jpg"
  },
  {
    "first_name":"Danny",
    "avatar":"image.jpg"
  },
  {
    "first_name":"Jimmy",
    "avatar":"image.jpg"
  },
  {
    "first_name":"Brandon",
    "avatar":"image.jpg"
  },
  {
    "first_name":"John",
    "avatar":"image.jpg"
  },
  {
    "first_name":"James",
    "avatar":"image.jpg"
  },
  {
    "first_name":"Matt",
    "avatar":"image.jpg"
  }
]

var g = {
  "name": "Pandemic",
  "release_date": 2003,
  "min_players":2,
  "max_players":4,
  "estimated_play_time":45,
  "mfg_suggested_min_ages":10,
  "tags":["family","strategy","competitive"],
  "production": {
    "designers":["Matt Leacock"],
    "publishers":["Z-Man Games","",""]
  },
  "short_description":"Four diseases have broken out in the world and it is up to a team of specialists in various fields to find cures for these diseases before mankind is wiped out. Players must work together playing to their characters' strengths and planning their strategy of eradication before the diseases overwhelm the world with ever-increasing outbreaks."
  "extended_description":"more...",
  "videos":[],
  "expansions":[],
  "related_games":[],
  "images": {
    "cover":"image.jpg",
    "box":"image.jpg"
  },
  "prices":{
    "prizm_digital":4.99,
    "physical_boxed":32.99
  },
  "options": {
    "Difficulty":[
      "Beginner","Normal","Hard"
    ]
  }
}

var p =
