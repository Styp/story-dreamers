<script>
    import {createEventDispatcher} from "svelte";

    const dispatch = createEventDispatcher();

    function forward(event) {
        dispatch('click', event.detail);
    }
</script>

<button type="button"
        on:click={forward}
        class="text-white !bg-gradient-to-br from-purple-600 to-blue-500 hover:!bg-gradient-to-b focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg px-5 py-2.5 text-center mr-2 mb-2">
    <slot></slot>
</button>