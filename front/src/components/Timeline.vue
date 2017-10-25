
<template>
    <div>
        <h2>{{this.title}}</h2>
        <div class="row">
            <div class="col-sm-12">
                <div class="from-group col-sm-4 float-right" style="margin-right: 15px;">
                    <label for="filterInput">Buscar</label>
                    <input v-model="busqueda" class="form-control" id="filterInput" placeholder="Términos de Búsqueda">
                </div>
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
  Un componente de una sola página en vue está estructurado de la siguiente manera:
  Un Template (arriba), donde se escribe el código html con propiedades de Vue.

  Un código de Script (este), es donde escribimos nuestro código JS y vue
  elementos (datos, métodos, calculados, etc.)

  Un estilo donde se escribe css.
  El alcance de este CSS también se define allí
*/

/*
    Este componente representa varios "TimelineBlocks" basados ​​en el "eventData"
    En la página, este componente es la Línea en el medio
*/

import TimelineBlock from "./TimelineBlock.vue";

export default {
  /*
    Como componente de un solo archivo, los datos deben ser una función.
    Los atributos del componente se declaran aquí.
    */
  data() {
    return {
      talks: [],
      title: "",
      busqueda: ""
    };
  },
  components: {
    TimelineBlock
  },
  /*
    Las propiedades computadas (computed) son métodos que se ejecutarán una vez y no
    seran llamadas nuevamente hasta que una variable involucrada en el
    proceso, cambie. Por ejemplo, si "this.$store.getters.talksViernes" cambia
    fetchData se activará.
    */
  computed: {
    fetchData() {
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
      return charlas.filter(x => {
        /** 
       * @name P05 - Filtro en timeline
       * @description Implementar un filtro de busqueda y que retorne
       * solo los elementos que se buscan en la vista
       */
        return [];
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
        Utiliza el operador de propagación para transformar de conjunto a matriz
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
