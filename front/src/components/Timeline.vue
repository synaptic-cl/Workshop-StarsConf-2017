<template>
    <div>
        <br>
        <h2 v-if="title">
            {{title}}</h2>
        <section id="cd-timeline">
            <TimelineBlock :key="item" v-for="item in talks" :eventData="item"></TimelineBlock>
        </section>
    </div>
</template>

<script>

import TimelineBlock from './TimelineBlock.vue';

export default {
    data() {
        return {
        }
    },
    props: [
        'talks', 'title'
    ],
    components: {
        TimelineBlock
    },
}
</script>

<style>

</style>
