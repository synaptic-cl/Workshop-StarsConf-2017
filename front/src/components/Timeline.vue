
<template>
    <div>
        <h2>{{this.title}}</h2>
        <div class="pull-right">
            <div class="from-group" style="margin-right: 15px;">
                <label for="filterInput">Buscar</label>
                <input v-model="busqueda" class="form-control" id="filterInput" placeholder="Términos de Búsqueda">
            </div>
        </div>
        <section id="cd-timeline" class="cd-container">
            <TimelineBlock :key="item.id" v-for="item in this.processData" :eventData="item"></TimelineBlock>
        </section>
        <br><br>
    </div>
</template>

<script>
/*
    A single page component in vue is scaffolded as follows:
    A template (above this), where the html code is written.

    A Script code (this one), is were we write our JS code and vue
    elements (data, methods, computed, etc)

    A Style tage where css is written. 
    The scope of this css is also defined there
*/

/*
    This component renders several "TimelineBlocks" based on the "eventData"
    In the page, this component is the Line in the middle
*/

import TimelineBlock from "./TimelineBlock.vue";

export default {
  /*
        As a single file component, data should be a function.
        Component's attributes are declared here.
    */
  data() {
    return {
      talks: [],
      title: "",
      busqueda: ""
    };
  },
  /*
        Register Component "TimelineBlock"
    */
  components: {
    TimelineBlock
  },
  /*
        Computed property are methods that will run once and it will
        not be called again until a variable, involved in the 
        process, change. For instance, if "this.$store.getters.talksViernes" changes
        fetchData will be triggered.
    */
  computed: {
    fetchData() {
      /*
                Fetch data will watch changes in the Store, so 
                the data rendered will be up to date.  
            */
      let charlas = [];
      switch (this.$route.params.dia) {
        case "viernes":
          this.title = "Programación Día Viernes 03 de Noviembre";
          charlas = this.$store.getters.talksViernes;
          break;
        case "sabado":
          this.title = "Programación Día Sábado 04 de Noviembre";
          charlas = this.$store.getters.talksSabado;
          break;
        default:
          this.title = "No hay data ups!";
          charlas = this.$store.state.noData;
      }
      /*
                Modify this line if you want to add a filter
            */
      /* P07 */
      return charlas.filter(x => {
        let current_busqueda = this.busqueda.toLowerCase();
        let search_speaker =
          x.speaker != null
            ? x.speaker.name.toLowerCase().includes(this.busqueda)
            : false;
        let search_title = x.name.toLowerCase().includes(current_busqueda);
        let search_room = x.room.toLowerCase().includes(this.busqueda);
        let search_category = x.category.toLowerCase().includes(this.busqueda);
        return search_speaker || search_category || search_title || search_room;
      });
    },
    processData() {
      let charlas = this.fetchData;
      let timeSlot = charlas.map(x => {
        if (x.category != "TALLERES") {
          return (
            x.timeSlot.start.slice(0, 5) + " - " + x.timeSlot.end.slice(0, 5)
          );
        }
      });
      /*
        Uses spread operator to transform from Set to Array
      */
      timeSlot = [...new Set(timeSlot)];
      let talksPerTimeSlot = [];
      timeSlot.forEach(x => {
        talksPerTimeSlot.push(
          charlas.filter(y => {
            return (
              x.includes(y.timeSlot.start.slice(0, 5)) &&
              x.includes(y.timeSlot.end.slice(0, 5))
            );
          })
        );
      });
      return talksPerTimeSlot;
    }
  }
};
</script>

<style>

</style>
