
const nomCtrl = document.querySelector("#simulation-1 input[name='nom']");
const ageCtrl = document.querySelector("#simulation-1 input[name='age']");
const app = new Vue({
  el: "#simulation-1",
  data: {
    step: -1,
    nom: 'Raed',
    age: 16,
    message: ''
  },
  methods: {
    simuler: function (step) {
      this.step = step;
      if (step == 0) {  
        Vue.nextTick(() => this.$refs.nom.focus());
      } else if (step == 1) {        
        Vue.nextTick(() => this.$refs.age.focus());
      } else if (step == 2) {
        if (this.age > 18) {
          this.message = "Vous êtes majeur depuis " + (this.age - 18) + " ans";
        } else if (this.age < 18) {
          this.message = "Vous serez majeur dans " + (18 - this.age) + " ans";
        } else {
          this.message = "Vous êtes majeur à partir de cette année";
        }
      }
    }
  }
});