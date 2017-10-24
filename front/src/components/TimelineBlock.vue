<template>
    <div class="cd-timeline-block" :id="id">
        <div class="cd-timeline-img">
            <img v-if="timeNowImage" :src="timeNowImage" />
            <img v-else :src="setBaseImage" />
        </div>
        <div class="cd-timeline-content card">
            <div :key="item.id" v-for="item in eventData">
              <hr v-if="eventData.length > 0 && item != eventData[0]">
              <div id="info-state" v-if="eventData.length > 0 && item == eventData[0]">
                <span class="float-right badge" :class="[badgeStyle]">{{title}}</span>
              </div>
              <h2>{{item.name}}</h2>
              {{getTimeStore}}
              <p v-if="item.speaker!=null">Orador: {{item.speaker.name}}</p>
              <p>{{ setRoom(item) }}</p>
              <!--
              -#  /**
              -#  * @requires P03 - Muestra la Categoria
              -#  */
              -->
            </div>
            <a href="#0" class="cd-read-more" @click="showModal = true">Más Información</a>
            <!-- P01 - Completar información del modal -->
              <modal v-if="showModal" @close="showModal = false" :information="eventData"></modal>
            <span class="cd-date">
                <strong>Hora de Inicio</strong>: {{eventData[0].timeSlot.start.slice(0, 5)}}<br>
                <strong>Hora de Término</strong>: {{eventData[0].timeSlot.end.slice(0, 5)}}
            </span> 
        </div>
    </div>
</template>

<script>
import Modal from "./Utils/Modal.vue";
/*
    This component is the card itself, it relies on Sebastiano Guerriero's 
    Vertical-timeline (https://codyhouse.co/gem/vertical-timeline/)
*/
export default {
  data() {
    return {
      showModal: false,
      title: "",
      dataModal: "No información",
      badgeStyle: "badge-danger",
      baseImage: "",
      timeNowImage: null,
      id: this.eventData[0].id,
      scroll: true
    };
  },
  components: {
    Modal: Modal
  },
  props: ["eventData"],
  methods: {
    isActive(timenow) {
      const timeStart = this.eventData[0].timeSlot.start.slice(0, 5);
      const timeEnd = this.eventData[0].timeSlot.end.slice(0, 5);

      /**
       * @name P02 - Marca la posición actual en el timeline.
       * @name P04 - Has un scroll cuando ya no veas la marca en el timeline.
       * @description En este desafio, se debe implementar la funcionalidad que devuelva cual charla esta finalizada,
       * en curso o proxima, se debe poder ver reflajado en el html.
       * 
       * ademas de eso generar una efecto que permita llevarnos a la charla actual, solo cuando se ingresa por primera ves a la pagina 
       * (agrega esta imagen a charlas en curso)
       image  http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/128/Actions-rating-icon.png
       */
    },
    setRoom: function(item) {
      /* This computed sets the 'pretty' room's name in the card */
      let room = "";
      switch (item.room) {
        case "DOS":
          room = "Sala 2";
          break;
        case "PRINCIPAL":
          room = "Sala Principal";
          break;
        case "Sala Chica":
          room = "CHICA";
        case "TALLERES":
          room = "Sala Talleres";
        default:
          room = "-";
          break;
      }
      return room;
    }
  },
  computed: {
    getTimeStore: function() {
      return this.isActive(this.$store.getters.getTimeNow);
    },
    setBaseImage: function() {
      let baseImage = "";
      switch (this.eventData.category) {
        case "Web & Mobile":
          baseImage = "/src/assets/img/categories/Workshop-icon.png";
          break;
        case "Mix":
          baseImage = "/src/assets/img/categories/Arrow-Mix-icon.png";
          break;
        case "Developer Tools":
          baseImage = "/src/assets/img/categories/Workshop-icon.png";
        case "Taller":
          baseImage = "/src/assets/img/categories/Workshop-icon.png";
        default:
          baseImage = "/src/assets/img/categories/pitr-Coffee-cup-icon.png";
          break;
      }
      return baseImage;
    }
  }
};
</script>

<style scoped>
#info-state {
  padding: 0 0 1em 0;
}

.badge-warning {
  color: #ffffff;
  background-color: #ffc107;
}
</style>
