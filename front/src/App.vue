<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <p v-if="loading">Loading...</p>
    <Schedule :time-slots="timeSlots"
      :room-names="['Sala 2', 'Sala Principal', 'Sala Chica', 'Sala Talleres']"
      :room-ids="['DOS', 'PRINCIPAL', 'CHICA', 'TALLERES']"
      :grid="grid"
      >
    </Schedule>
  </div>
</template>

<script>
import axios from 'axios';
import ALL_TALKS from './constants';
import Schedule from './components/Schedule.vue';

export default {
  name: 'app',
  data() {
    return {
      msg: 'Horario StarsConf 2017',
      loading: true,
      timeSlots: {},
      talks: [],
      grid: {},
    }
  },
  components: {
    Schedule: Schedule,
  },
  methods: {
    loadSchedule() {
      console.log('Load schedule');
      axios.get(`http://localhost:8000/graphql?query=${ALL_TALKS}`)
        .then((response) => {
          console.log(response);
          this.talks = response.data.data.allTalks.map((talk) => {
            if(talk.speaker) {
              talk.speaker = talk.speaker.name;
            }
            return talk;
          });

          this.talks.forEach((talk) => {
            this.timeSlots[talk.timeSlot.id] = talk.timeSlot;
            if(!this.grid[talk.timeSlot.id]){
              this.grid[talk.timeSlot.id] = {};
            }

            this.grid[talk.timeSlot.id][talk.room] = talk;
          })
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
