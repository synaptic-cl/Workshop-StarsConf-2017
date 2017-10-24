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
            </div>
            <a href="#0" class="cd-read-more" @click="showModal = true">Más Información</a>
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
      if (
        Date.parse("01/01/2011 " + timenow + ":00") >=
          Date.parse("01/01/2011 " + timeStart + ":00") &&
        Date.parse("01/01/2011 " + timenow + ":00") <=
          Date.parse("01/01/2011 " + timeEnd + ":00")
      ) {
        this.title = "Charla en Curso";
        this.timeNowImage =
          "/src/assets/img/categories/Actions-rating-icon.png";
        this.badgeStyle = "badge-success";

        var nav = $("#" + this.id);
        if (nav.length && this.scroll) {
          this.scroll = false;
          $("html,body").animate(
            {
              scrollTop: nav.offset().top
            },
            () => {
              $("html,body").stop(true, true);
            }
          );
        }
      } else if (
        Date.parse("01/01/2011 " + timenow + ":00") <
        Date.parse("01/01/2011 " + timeEnd + ":00")
      ) {
        this.timeNowImage = null;
        this.title = "Proxima Charla";
        this.badgeStyle = "badge-warning";
      } else {
        this.timeNowImage = null;
        this.title = "Charlas Finalizadas";
        this.badgeStyle = "badge-danger";
      }
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
