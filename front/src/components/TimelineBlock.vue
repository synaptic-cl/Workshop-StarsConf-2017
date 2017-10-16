<template>
    <div class="cd-timeline-block">
        <div class="cd-timeline-img">
            <img v-if="eventData.category==='Web & Mobile'" src="http://www.75squared.co.uk/wp-content/uploads/2015/08/mobile-icon.png">
            <img v-else-if="eventData.category==='Mix'" src="http://icons.iconarchive.com/icons/iconsmind/outline/512/Arrow-Mix-icon.png">
            <img v-else-if="eventData.category==='Developer Tools'" src="https://image.freepik.com/free-icon/tools-cross-settings-symbol-for-interface_318-48264.jpg">
            <img v-else-if="eventData.category==='Taller'" src="http://smsvaranasi.com/wp-content/uploads/2016/01/Workshop-icon.png">
            <img v-else src="https://openclipart.org/image/2400px/svg_to_png/22305/pitr-Coffee-cup-icon.png">
        </div>
        <div class="cd-timeline-content">
            <h2>{{eventData.name}}</h2>
            <p v-if="eventData.speaker!=null">Orador: {{eventData.speaker.name}}</p>
            <p v-else-if="eventData.room='DOS'">Sala 2</p>
            <p v-else-if="eventData.room='PRINCIPAL'">Sala Principal</p>
            <p v-else-if="eventData.room='CHICA'">Sala Chica</p>
            <p v-else-if="eventData.room='TALLERES'">Sala Talleres</p>
            <a href="#0" class="cd-read-more">Más Información</a>
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
    props: ['eventData']
}
</script>

<style>

</style>
