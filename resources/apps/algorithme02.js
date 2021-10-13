
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

const app1 = new Vue({
  el: "#simulation-2",
  data: {
    step: -1,
    qte: 5,
    argent: 5000,
    message: ''
  },
  methods: {
    simuler: function (step) {
      this.step = step;
      if (step == 0) {  
        Vue.nextTick(() => this.$refs.qte.focus());
      } else if (step == 1) {        
        Vue.nextTick(() => this.$refs.argent.focus());
      } else if (step == 2) {
        const total = this.qte * 800;
        if (this.argent > total) {
          this.message = "Monnaie = " + (this.argent - total);
        } else if (this.argent < total) {
          this.message = "Manquant = " + (total - this.argent);
        } else {
          this.message = "A bientôt";
        }
      }
    }
  }
});