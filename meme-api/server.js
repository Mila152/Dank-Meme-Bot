// server.js
// where your node app starts

// init project
const express = require('express');
const app = express();
const reddit = require('random-puppy');
const axios = require('axios');

const PORT = 80; //for goorm
//const PORT = process.env.PORT || 80; // for heroku

const meme_lists = {
    dank: [
        "dankmemes" //Dank
    ],
    normie: [
        "comedy"
    ],
    moderate: [
        "memes"
    ],
    furry: [
        "furry_irl"
    ],
    it: [
        "ITMemes"
    ],
    edgy: [
        "iamveryedgy"
    ],
    wholesome: [
        "UnexpectedlyWholesome"
    ],
    christian: [
        "dankchristianmemes"
    ],
    art: [
        "classicalartmemes"
    ],
    history: [
        "HistoryMemes"
    ],
    anime: [
        "Animemes"
    ],
    fourchan: [
        "4chan"
    ]
}
function int(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
function GetMeme(category) {
  return new Promise((fulfill, reject) => {
    var list = meme_lists[category];
    var iD = 0;//int(0, list.length);
    var sel = list[iD];
    reddit(sel).then(m => {
      fulfill(m);
    }).catch(reject);
  });
}

app.use(express.static('public'));
app.get('/', function(req, res) {
  res.status(200).sendFile(__dirname + '/views/index.html');
});

app.get('/dank', function(req, res) {
  GetMeme("dank").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "dank",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "dank", error: e, retry: "5s" });
  });
});

app.get('/furry', function(req, res) {
  GetMeme("furry").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "furry",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "furry", error: e, retry: "5s" });
  });
});

app.get('/it', function(req, res) {
  GetMeme("it").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "IT",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "IT", error: e, retry: "5s" });
  });
});

app.get('/edgy', function(req, res) {
  GetMeme("edgy").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "edgy",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "edgy", error: e, retry: "5s" });
  });
});

app.get('/wholesome', function(req, res) {
  GetMeme("wholesome").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "wholesome",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "wholesome", error: e, retry: "5s" });
  });
});

app.get('/christian', function(req, res) {
  GetMeme("christian").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "christian",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "christian", error: e, retry: "5s" });
  });
});

app.get('/art', function(req, res) {
  GetMeme("art").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "art",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "art", error: e, retry: "5s" });
  });
});

app.get('/history', function(req, res) {
  GetMeme("history").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "history",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "history", error: e, retry: "5s" });
  });
});

app.get('/anime', function(req, res) {
  GetMeme("anime").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "anime",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "anime", error: e, retry: "5s" });
  });
});

app.get('/fourchan', function(req, res) {
  GetMeme("fourchan").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "4chan",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "4chan", error: e, retry: "5s" });
  });
});

app.get('/normie', function(req, res) {
  GetMeme("normie").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "normie",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "normie", error: e, retry: "5s" });
  });
});

app.get('/moderate', function(req, res) {
  GetMeme("moderate").then(meme => {
    if (meme) {
      res.status(200).send({ endpoint: "moderate",  meme: meme });
    } else {
      throw new Error("Internal error");
    }
  }).catch((e) => {
    res.status(500).send({ endpoint: "moderate", error: e, retry: "5s" });
  });
});

app.use(function(req, res) {
  res.status(404).send("<html><head><script>window.location.href='/'</script></head><body><center>Endpoint not found</center></body></html>");
});

const listener = app.listen(PORT, function() {
  console.log('Your app is listening on port ' + listener.address().port);
});
