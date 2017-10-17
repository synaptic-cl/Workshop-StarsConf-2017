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
</style>
