<template>
    <div class="cd-timeline-block">
        <div class="cd-timeline-img">
            <img :src="setBaseImage" />
        </div>
        <div class="cd-timeline-content card">
            <div id="info-state">
                <span class="float-right badge" :class="[badgeStyle]">{{title}}</span>
            </div>
            <h2>{{eventData.name}}</h2>
            {{getTimeStore}}
            <p v-if="eventData.speaker!=null">Orador: {{eventData.speaker.name}}</p>
            <p>{{ setRoom }}</p>
            <a href="#0" class="cd-read-more" @click="showModal = true">Más Información</a>
            <modal v-if="showModal" @close="showModal = false" :information="emptyList">
            </modal>
            <span class="cd-date">
                <strong>Hora de Inicio</strong>: {{eventData.timeSlot.start.slice(0, 5)}}<br>
                <strong>Hora de Término</strong>: {{eventData.timeSlot.end.slice(0, 5)}}
            </span>
        </div>
    </div>
</template>

<script>
import Modal from './Utils/Modal.vue';
/*
    This component is the card itself, it relies on Sebastiano Guerriero's 
    Vertical-timeline (https://codyhouse.co/gem/vertical-timeline/)
*/
export default {
    data() {
        return {
            showModal: false,
            title: '',
            badgeStyle: 'badge-danger',
            /* P03 Pass data to the modal
            Recomended: Look Orador's information */
            emptyList: []
        }
    },
    components: {
        Modal: Modal
    },
    props: ['eventData'],
    methods: {
        isActive(timenow) {
            const timeStart = this.eventData.timeSlot.start.slice(0, 5)
            const timeEnd = this.eventData.timeSlot.end.slice(0, 5)
            /*
            P04 crearlogica que devuela los tag de charla actual, proxima y finalizada
            */
            this.title = 'Charlas Finalizadas'
            this.badgeStyle = 'badge-danger'
        }
    },
    computed: {
        getTimeStore: function() {
            return this.isActive(this.$store.getters.getTimeNow)
        },
        setRoom: function() {
            /* This computed sets the 'pretty' room's name in the card */
            let room = ''
            switch (this.eventData.room) {
                case 'DOS':
                    room = 'Sala 2'
                    break;
                case 'PRINCIPAL':
                    room = 'Sala Principal'
                    break
                case 'Sala Chica':
                    room = 'CHICA'
                case 'TALLERES':
                    room = 'Sala Talleres'
                default:
                    room = '-'
                    break;
            }
            return room
        }
        , setBaseImage: function() {
            let baseImage = ''
            switch (this.eventData.category) {
                case 'Web & Mobile':
                    baseImage = "http://smsvaranasi.com/wp-content/uploads/2016/01/Workshop-icon.png"
                    break;
                case 'Mix':
                    baseImage = "http://icons.iconarchive.com/icons/iconsmind/outline/512/Arrow-Mix-icon.png"
                    break
                case 'Developer Tools':
                    baseImage = "http://smsvaranasi.com/wp-content/uploads/2016/01/Workshop-icon.png"
                case 'Taller':
                    baseImage = "http://smsvaranasi.com/wp-content/uploads/2016/01/Workshop-icon.png"
                default:
                    baseImage = ""
                    break;
            }
            return baseImage
        }
    }
}
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
