<template>
  <div>
    <header>
      <h1>Horario StarsConf 2017
        <i class="fa fa-calendar" aria-hidden="true"></i>
      </h1>
    </header>
    <ul class="nav nav-tabs justify-content-center" id="navigation-ul">
      <li class="nav-item">
        <router-link to="/agenda/viernes" class="nav-link" active>Programación Viernes</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/agenda/sabado" class="nav-link">Programación Sábado</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/nosotros" class="nav-link">Acerca de Synaptic</router-link>
      </li>
    </ul>
    <clock></clock>
  </div>
</template>

<script>
import Clock from './Utils/Clock.vue';

export default {
  name: 'appheader',
  components: {
    clock: Clock
  }
};
</script>

<style scope>
header {
  height: 300px !important;
  line-height: 300px !important;
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
    height: 300px !important;
    line-height: 300px !important;
  }
  header h1 {
    font-size: 24px;
    font-size: 2rem;
  }
}

#navigation-ul {
  background: #303e49;
}

#navigation-ul li a {
  color: #ffffff;
}

.router-link-active {
  background: #e9f0f5;
  color: #303e49 !important;
}

.nav-tabs .nav-link:focus,
.nav-tabs .nav-link:hover {
  border-color: #e9f0f5 #e9f0f5 #e9f0f5;
}
</style>
