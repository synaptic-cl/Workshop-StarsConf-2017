<template>
    <section id="cd-timeline">
        <TimelineBlock v-for="item in talks" :eventData="item"></TimelineBlock>
    </section>
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
