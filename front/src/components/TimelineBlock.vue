<template>
    <div class="cd-timeline-block">
        <div class="cd-timeline-img">
            <img v-if="eventData.category==='Web & Mobile'" src="http://www.75squared.co.uk/wp-content/uploads/2015/08/mobile-icon.png">
            <img v-else-if="eventData.category==='Mix'" src="http://icons.iconarchive.com/icons/iconsmind/outline/512/Arrow-Mix-icon.png">
            <img v-else-if="eventData.category==='Developer Tools'" src="https://access.redhat.com/webassets/avalon/g/dev-tools-200.png">
            <img v-else-if="eventData.category==='Taller'" src="http://smsvaranasi.com/wp-content/uploads/2016/01/Workshop-icon.png">
            <img v-else src="https://openclipart.org/image/2400px/svg_to_png/22305/pitr-Coffee-cup-icon.png">
        </div>
        <div class="cd-timeline-content card">
            <h2>{{eventData.name}}</h2>
            <p v-if="eventData.speaker!=null">Orador: {{eventData.speaker.name}}</p>
            <p>{{ setRoom }}</p>
            <a href="#0" class="cd-read-more" @click="showModal = true">Más Información</a>
            <modal v-if="showModal" @close="showModal = false" :information="eventData">
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

export default {
    data() {
        return {
            showModal: false
        }
    },
    components: {
        Modal: Modal
    },
    props: ['eventData'],
    computed: {
        setRoom: function() {
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
    }
}
</script>

<style>

</style>
