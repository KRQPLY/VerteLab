<template>
  <div class="responsive-container">
    <div class="login">
      <header>
        <button
          class="sign-up-button"
          :class="{ active: !registered }"
          @click="registered = false"
        >
          Sign Up
        </button>
        <button
          class="sign-in-button"
          :class="{ active: registered }"
          @click="registered = true"
        >
          Sign In
        </button>
      </header>
      <SignForm v-if="!registered" />
      <SignForm v-else is-sign-in />
    </div>
  </div>
</template>

<script setup lang="ts">
import SignForm from "@/components/SignForm.vue";
import { ref } from "vue";

const registered = ref(true);
</script>

<style scoped lang="scss">
.login {
  margin-top: 20px;
  border: 1px solid $color-athens-gray;
  border-radius: 4px;
  display: flex;
  flex-direction: column;

  header {
    display: flex;
    justify-content: center;

    .sign-up-button {
      width: 100%;
      border: none;
      border-right: 1px solid $color-athens-gray;
      border-bottom: 1px solid $color-athens-gray;
    }

    .sign-in-button {
      width: 100%;
      border: none;
      border-left: 1px solid $color-athens-gray;
      border-bottom: 1px solid $color-athens-gray;
    }

    button {
      height: 40px;
      cursor: pointer;
      font-family: Poppins;
      background: none;
      &.active {
        border: none;
      }
    }
  }
}
</style>
