const positions = [
  [0, 1, 2, 3, 4, 5, 6],
  [19, 20, 21, 22, 23, 24, 7],
  [18, 31, 32, 33, 34, 25, 8],
  [17, 30, 29, 28, 27, 26, 9],
  [16, 15, 14, 13, 12, 11, 10],
];

const app = new Vue({
  el: "#jeu-oie",
  data: {
    target_pos: 32,
    pos_oie: 0,
    dice1_face: 3,
    dice2_face: 3,
    movements: [],
    canClicDice: true,
    winner_message: "Gagné"
  },
  computed: {
    first_dice: function() {
      return {
        [`de${this.dice1_face}`]: true
      };
    },
    second_dice: function() {
      return {
        [`de${this.dice2_face}`]: true
      };
    }
  },
  mounted: function() {
    this.reset();
    this.$forceUpdate();
  },
  methods: {
    reset: function() {
      this.pos_oie = 0;
      this.canClicDice = true;
      this.movements = [];
      this.rollDices();
    },
    rollDices: function() {
      this.dice1_face = 1 + Math.floor(Math.random() * 6);
      this.dice2_face = 1 + Math.floor(Math.random() * 6);
    },
    gameEnded: function() {
      return this.pos_oie == this.target_pos;
    },
    clicked: function() {
      if (!this.canClicDice || this.gameEnded()) {
        return;
      }

      this.rollDices();
      const sum_dices = this.dice1_face; // + this.dice2_face;
      let new_pos;
      if (this.pos_oie + sum_dices > this.target_pos) {
        new_pos = this.pos_oie - sum_dices;
        this.movements.push(`Dé ${sum_dices} : Reculer de ${this.pos_oie} à ${new_pos}`);
      } else {
        new_pos = this.pos_oie + sum_dices;
        this.movements.push(`Dé ${sum_dices} : Avancer de ${this.pos_oie} à ${new_pos}`);
      }
      this.canClicDice = false;
      const timerDuration = 300;
      const moveOie = () => {
        if (this.pos_oie > new_pos) {
          this.pos_oie--;
        } else if (this.pos_oie < new_pos) {
          this.pos_oie++;
        }
        this.canClicDice = this.pos_oie == new_pos;
        if (this.gameEnded()) {
          this.movements.push("Gagné");
        }
        if (!this.canClicDice) setTimeout(moveOie, timerDuration);
      };
      moveOie();
      // this.pos_oie = new_pos;
    }
  }
});