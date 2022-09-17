<script lang="ts">
    export let position: 'left'|'right' = 'left'
    export let skew: string = ''
</script>

<div class="absolute top-0 left-0 bg-amber-50 w-full  shadow shadow-black/40 overflow-hidden
            {position==='left'?`${skew} origin-top-right rounded-l-2xl`:`-${skew} origin-top-left rounded-r-2xl`}">
    <div class="aspect-h-1 aspect-w-1">
        <slot></slot>
    </div>
</div>