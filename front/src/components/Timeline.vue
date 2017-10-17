<template>
    <div>
        <br>
        <h2>{{this.title}}</h2>
        <section id="cd-timeline">
            <TimelineBlock :key="item.id" v-for="item in this.talks" :eventData="item"></TimelineBlock>
        </section>
        <pre>{{this.talks}}</pre>
    </div>
</template>

<script>

import TimelineBlock from './TimelineBlock.vue';

export default {
    data() {
        return {
            talks: [],
            title: "",
            dia: ""
        }
    },
    components: {
        TimelineBlock
    },
    watch: {
        '$route'(to, from) {
            this.dia = to.params.dia;
            switch (this.dia) {
                case "viernes":
                    this.talks = this.$store.state.talksViernes;
                    this.title = "Programación Día Viernes 03 de Noviembre"
                    break;
                case "sabado":
                    this.talks = this.$store.state.talksSabado;
                    this.title = "Programación Día Sábado 04 de Noviembre"
                    break;
                default:
                    this.talks = this.$store.state.talksViernes;
                    this.title = "Programación Día Viernes 03 de Noviembre"
            }
        }
    },
    route: {
        canReuse: false
    }
}
</script>

<style>

</style>
