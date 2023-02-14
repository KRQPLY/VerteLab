<template>
  <header>
    <div class="title"><SpineIcon /> VerteLab</div>
    <div class="logout">Logout</div>
  </header>
</template>

<script setup lang="ts">
import SpineIcon from "@/components/icons/SpineIcon.vue";
</script>

<style scoped lang="scss">
header {
  padding: 10px 20px;
  background-color: $color-orange;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .title {
    font-size: 30px;
    font-weight: bold;
    display: flex;
    align-items: center;
  }

  .logout {
    cursor: pointer;
  }
}
</style>
