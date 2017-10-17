<template>
    <div>
        <br>
        <h2>{{this.title}}</h2>
        <section id="cd-timeline" class="cd-container">
            <TimelineBlock :key="item.id" v-for="item in this.fetchData" :eventData="item"></TimelineBlock>
        </section>
        {{$data}}
    </div>
</template>

<script>

import TimelineBlock from './TimelineBlock.vue';
import { mapGetters } from 'vuex';

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
    computed: {
        fetchData() {
            switch (this.$route.params.dia) {
                case "viernes":
                    this.title = "Programación Día Viernes 03 de Noviembre";
                    return this.$store.getters.talksViernes
                    break;
                case "sabado":
                    this.title = "Programación Día Sábado 04 de Noviembre";
                    return this.$store.getters.talksSabado
                    break;
                default:
                    this.title = "No hay data ups!"
                    return this.$store.state.noData;
            }
        }
    }
}
</script>

<style>

</style>
