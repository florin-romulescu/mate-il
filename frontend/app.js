const express = require("express");
const axios = require("axios");
const path = require("path");
const app = express();

const port = 3000;

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "resurse")));

console.log(path.join(__dirname, "views"));

const api_search = async (q, author = "") => {
  let url = `http://localhost:8000/api/posts/search?format=json&q=${q}`;
  if (author) {
    url += `&author=${author}`;
  }
  let response = await axios.get(url);
  return response.data;
};

app.get("/test", async (req, res) => {
  let data = await api_search("Postare");
  return res.json(data);
});

app.get("/", (req, res) => {
  res.render("index");
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
