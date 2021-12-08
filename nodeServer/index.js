const express = require("express");
const app = express();
const fs = require("fs");
const cors = require("cors");
app.use(express.static("public"));

app.use(cors());
app.get("/", (req, res) => {
  fs.readFile("./db.json", (err, json) => {
    let obj = JSON.parse(json);
    res.json(obj);
  });
});

const port = 3000;
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
