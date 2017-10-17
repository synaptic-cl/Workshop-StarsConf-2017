<template>
    <div class="cd-timeline-block">
        <div class="cd-timeline-img">
            <img v-if="eventData.category==='Web & Mobile'" src="http://www.75squared.co.uk/wp-content/uploads/2015/08/mobile-icon.png">
            <img v-else-if="eventData.category==='Mix'" src="http://icons.iconarchive.com/icons/iconsmind/outline/512/Arrow-Mix-icon.png">
            <img v-else-if="eventData.category==='Developer Tools'" src="https://image.freepik.com/free-icon/tools-cross-settings-symbol-for-interface_318-48264.jpg">
            <img v-else-if="eventData.category==='Taller'" src="http://smsvaranasi.com/wp-content/uploads/2016/01/Workshop-icon.png">
            <img v-else src="https://openclipart.org/image/2400px/svg_to_png/22305/pitr-Coffee-cup-icon.png">
        </div>
        <div class="cd-timeline-content card">
            <h2>{{eventData.name}}</h2>
            <p v-if="eventData.speaker!=null">Orador: {{eventData.speaker.name}}</p>

            <p v-if="eventData.room!=''">
                <strong>Lugar</strong>:
                <span v-if="eventData.room='DOS'">Sala 2</span>
                <span v-else-if="eventData.room='PRINCIPAL'">Sala Principal</span>
                <span v-else-if="eventData.room='CHICA'">Sala Chica</span>
                <span v-else-if="eventData.room='TALLERES'">Sala Talleres</span>
            </p>
            <a href="#0" class="btn btn-dark">
                <i class="fa fa-plus" aria-hidden="true" /> Más</a>
            <span class="cd-date">
                <strong>Día</strong>: {{eventData.timeSlot.date}}<br>
                <strong>Inicio</strong>: {{eventData.timeSlot.start}}<br>
                <strong>Fin</strong>: {{eventData.timeSlot.end}}
            </span>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {}
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
