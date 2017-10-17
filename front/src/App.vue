<template>
  <div id="app">
    <app-header></app-header>
    <schedule></schedule>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Schedule from './components/Schedule.vue'
import Footer from './components/Footer.vue'
import TASKS_ALL from './graphql/AllTalks.gql'

export default {
  name: 'app',
  components: {
    appHeader: Header,
    Schedule: Schedule,
    appFooter: Footer
  }
}
</script>

<style>
html {
  height: 100%;
  box-sizing: border-box;
}

*,
*:before,
*:after {
  box-sizing: inherit;
}

body {
  position: relative;
  margin: 0;
  padding-bottom: 6rem;
  min-height: 100%;
  font-family: "Helvetica Neue", Arial, sans-serif;
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
