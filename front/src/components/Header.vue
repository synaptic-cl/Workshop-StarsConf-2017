<template>
  <div>
    <header>
      <h1>Horario StarsConf 2017
        <i class="fa fa-calendar" aria-hidden="true"></i>
      </h1>
    </header>
    <clock></clock>
  </div>
</template>

<script>
import Clock from './Clock/Clock.vue'

export default {
  name: 'appheader',
  components: {
    clock: Clock
  }
}
</script>

<style scope>
header {
  height: 260px;
  line-height: 260px;
  text-align: center;
  background: #303e49;
}

header h1 {
  color: white;
  font-size: 18px;
  font-size: 2rem;
}

@media only screen and (min-width: 1170px) {
  header {
    height: 260px;
    line-height: 260px;
  }
  header h1 {
    font-size: 24px;
    font-size: 2rem;
  }
}
</style>
