<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <p v-if="loading">Loading...</p>
    <ul>
      <li v-for="talk in talks">{{talk.timeSlot.date}} {{talk.timeSlot.start}} - {{talk.timeSlot.end}} {{talk.id}} - {{talk.name}} ({{talk.speaker && talk.speaker.name}})</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import ALL_TALKS from './constants';

export default {
  name: 'app',
  data() {
    return {
      msg: 'Horario StarsConf 2017',
      loading: true,
      talks: []
    }
  },
  methods: {
    loadSchedule() {
      console.log('Load schedule');
      axios.get(`http://localhost:8000/graphql?query=${ALL_TALKS}`)
        .then((response) => {
          console.log(response);
          this.talks = response.data.data.allTalks;
          this.loading = false;
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
