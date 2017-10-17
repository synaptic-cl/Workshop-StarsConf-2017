<template>
  <div>
    <header>
      <h1>Horario StarsConf 2017
        <i class="fa fa-calendar" aria-hidden="true"></i>
      </h1>
    </header>
    <clock></clock>
    <ul class="nav nav-tabs nav-fill justify-content-center">
      <li class="nav-item">
        <router-link to="/agenda/viernes" active-class="nav-link active">Programación Viernes</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/agenda/sabado" active-class="nav-link active">Programación Sábado</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/nosotros" active-class="nav-link active">Acerca de Synaptic</router-link>
      </li>
    </ul>
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
