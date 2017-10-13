<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="talk in talks">{{talk.id}} - {{talk.name}}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app',
  data() {
    return {
      msg: 'Horario StarsConf 2017',
      talks: []
    }
  },
  methods: {
    loadSchedule() {
      console.log('Load schedule');
      axios.get('http://localhost:8000/graphql?query={allTalks{id name}}')
        .then((response) => {
          console.log(response);
          this.talks = response.data.data.allTalks;
        });
    }
  },
  mounted() {
    this.loadSchedule();
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
