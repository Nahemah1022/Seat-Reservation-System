<template>
  <div>
  <form action="">
  <div class="sign-up-pop">
    <slot></slot>
  
  </div>
  </form>
  </div>
</template>

<script>
export default {
  name: 'PopupFrame',
 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
.sign-up-pop {
  margin: auto;
  display: flex;
  flex-direction: column;
  width: 35rem;
  height: 20rem;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  box-shadow:4px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  border-style: solid;
  border-width: 1px;
  border-color: #C4C4C4;
  font-family: '微軟正黑體';
}
</style>
