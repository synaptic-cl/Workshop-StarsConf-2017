<template>
  <div class="schedule" id="container-base">
    <p v-if="loading">Cargando Información del Evento...</p>
    <router-view></router-view>
  </div>
</template>

<script>
import TASKS_ALL from "../graphql/AllTalks.gql";
import TimeLine from "./Timeline.vue";

export default {
  name: "schedule",
  components: {
    TimeLine: TimeLine
  },

  data() {
    return {
      loading: true
    };
  },
  /**
   * Este componente usa la libreria de Apollo
   * para realizar las consultas a la API de GraphQL. 
   * Y además establecer los datos filtrados al estado de la aplicación.
   * @param query: Schema de la consulta enviada a la API
   * @param update: Personalizar el valor que se retorna, por ejemplo, si los nombres de los campos no coinciden.
   * @param result: Al finaliar exitosamente la consulta a la API
   * @param error: Si nos devuelve un error al ejecutar la consulta.
   */
  created() {
    this.$store.dispatch("setTime");
  },
  apollo: {
    tasks: {
      query: TASKS_ALL,
      update({ allTalks }) {
        this.$store.state.talksViernes = allTalks.filter(x => {
          return x.timeSlot.date == "2017-11-03";
        });
        this.$store.state.talksSabado = allTalks.filter(x => {
          return x.timeSlot.date == "2017-11-04";
        });
      },
      result({ data, loader, networkStatus }) {
        this.loading = false;
        return data;
      },
      error(error) {
        this.loading = false;
        console.error("We've got an error!", error);
      }
    }
  }
};
</script>


<style>
/* Import styles from "Vertical-timeline"  */

@import url("../assets/vertical-timeline/css/fonts.css");
@import url("../assets/vertical-timeline/css/reset.css");
@import url("../assets/vertical-timeline/css/style.css");

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
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
  content: "";
  position: absolute;
  top: 0;
  left: calc (100% - 150px / 2);
  height: 100%;
  width: 4px;
  background: #d7e4ed;
}

#container-base {
  margin-top: 50px;
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