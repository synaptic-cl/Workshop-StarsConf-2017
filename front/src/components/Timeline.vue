
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

import TimelineBlock from './TimelineBlock.vue';
import { mapGetters } from 'vuex';

export default {
    /*
        As a single file component, data should be a function.
        Component's attributes are declared here.
    */
    data() {
        return {
            talks: [],
            title: "",
            dia: ""
        }
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
            let charlas = []
            switch (this.$route.params.dia) {
                case "viernes":
                    this.title = "Programación Día Viernes 03 de Noviembre";
                    charlas = this.$store.getters.talksViernes
                    break;
                case "sabado":
                    this.title = "Programación Día Sábado 04 de Noviembre";
                    charlas = this.$store.getters.talksSabado
                    break;
                default:
                    this.title = "No hay data ups!"
                    charlas = this.$store.state.noData;
            }
            /*
                Modify this line if you want to add a filter
            */
            return charlas.filter((x) => { return true });
        }
    }
}
</script>

<style>

</style>
