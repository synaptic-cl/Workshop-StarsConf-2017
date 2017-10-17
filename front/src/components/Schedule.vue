<template>
  <div class="schedule">
    <time-line :talks="tasks"></time-line>
  </div>
</template>

<script>
import TASKS_ALL from '../graphql/AllTalks.gql'
import TimeLine from './Timeline.vue'

export default {
  name: 'schedule',
  components: {
    TimeLine: TimeLine
  },

  data() {
    return {
      tasks: [],
      addMode: false,
    }
  },
  apollo: {
    tasks: {
      query: TASKS_ALL,
      update({ allTalks }) {
        return allTalks
      },
    },
  },
}
</script>


<style>
@import url("https://fonts.googleapis.com/css?family=Droid+Serif|Open+Sans:400,700");
@import url("../assets/vertical-timeline/css/reset.css");
@import url("../assets/vertical-timeline/css/style.css");

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1,
h2 {
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

#cd-timeline {
  position: relative;
  padding: 2em 0;
  margin-top: 2em;
  margin-bottom: 2em;
}

#cd-timeline::before {
  /* this is the vertical line */
  content: '';
  position: absolute;
  top: 0;
  left: 18px;
  height: 100%;
  width: 4px;
  background: #d7e4ed;
}

.cssanimations .cd-timeline-img.is-hidden {
  visibility: hidden;
}

.cssanimations .cd-timeline-img.bounce-in {
  visibility: visible;
  animation: cd-bounce-1 0.6s;
}

@keyframes cd-bounce-1 {
  0% {
    opacity: 0;
    transform: scale(0.5);
  }
  60% {
    opacity: 1;
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
</style>