<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <p v-if="loading">Loading...</p>
    <div class="day" v-for="day in days">
      <Schedule :time-slots="timeSlotsOfDay(day)"
        :room-names="['Sala 2', 'Sala Principal', 'Sala Chica', 'Sala Talleres']"
        :room-ids="['DOS', 'PRINCIPAL', 'CHICA', 'TALLERES']"
        :grid="grid"
        :title="day"
        >
      </Schedule>
    </div>
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
      days: [],
      grid: {},
    }
  },
  components: {
    Schedule: Schedule,
  },
  methods: {
    loadSchedule() {
      console.log('Load schedule');
      let days = new Map();
      axios.get(`http://localhost:8000/graphql?query=${ALL_TALKS}`)
        .then((response) => {
          response.data.data.allTalks.forEach((talk) => {
            if(talk.speaker) {
              talk.speaker = talk.speaker.name;
            }

            let date = talk.timeSlot.date;
            days.set(date, "");
            this.days = Array.from(days.keys());
            this.talks.push(talk);
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
    },
    timeSlotsOfDay(day) {
      let slots = []
      Object.values(this.timeSlots).forEach(slot => {
        if(slot.date === day){
          slots.push(slot);
        }
      });
      return slots;
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
