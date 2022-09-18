<script lang="ts">
import Textinput from "./lib/components/Textinput.svelte";
import Button from "./lib/components/Button.svelte";
import {text, totalPages, currentPage, pages, loading} from "./lib/stores";
import {send_text_to_server} from "./lib/api";
import Story from "./lib/components/Story.svelte";
import {get} from "svelte/store";
import Loading from "./lib/components/Loading.svelte";

let currentPageValue;
let currentLoadingValue;

currentPage.subscribe(value =>  {
    currentPageValue=value
})

loading.subscribe(value => {
    currentLoadingValue=value
})

async function send_text(){
    loading.set(true)
    const response = await send_text_to_server(get(text))
    totalPages.set(response.length)
    pages.set(response)
}

</script>

<main>
    {#if currentLoadingValue}
        <Loading></Loading>
    {:else}
        {#if currentPageValue}
            <Story></Story>
        {:else}
            <h1 class="text-6xl tracking-wider text-center pt-4 pb-24">Story Dreamers</h1>
            <div class="grid grid-cols-2 gap-8">
                <Textinput></Textinput>
                <div class="text-lg max-w-md space-y-8 flex flex-col space-around pt-4">
                    <h2 class="text-3xl">Getting Started</h2>
                    <p>
                        Paste your favourite childhood stories on the left and we'll dream up the imagery for you.
                    </p>

                    <Button on:click={send_text}>Let's gooooo</Button>
                </div>
            </div>
        {/if}
    {/if}
</main>
