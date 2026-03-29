# Snake-Game
The classic snake game. Made with pygame.

You can check out my video tutorial series on how to create this game: https://www.youtube.com/watch?v=5tvER0MT14s&t=2s

# Requirements
- Python 3.x
- pygame

# Tasks : 
    - Learn about DQN networks

# tutorial on youtube to follow steps : 
`https://www.youtube.com/watch?v=L8ypSXwyBds`


# About the environnement
### what is it ?
The `Environement` is a space contains game control functions (move_up , down,...) , that its given to the model to ensure it controls the game based on the prediction.

## Agent : 
    - game
    - training : 
        * state = get_state()
        * action_ = get_move(state) :
            - model.predict()
        * reward , game_over , score_ = game.play_step(action)
        * new_state = get_state(game)
        * remember
        * model.train()
### Explaining : 
- ** state ** : array of  11 values , represents the game state : 
[danger_is_stright , danger_is_right , danger_is_left , direction_is_left , direction_is_riht , direction_is_up , direction_is_down , food_is_up , food_is_down , food_is_left , food_is_right].
`example : Screenshot_2.png` : 
state = [0,0,0,0,1,0,0,0,0,0,1]
- ** reward ** : helps the model understands the correct decision :
    * eat_food => +10
    * game_over => -10
    * else(nothing) => 0
- ** action ** : it stands for the predicted action to make (go left , right , stright..) : 
    * left = [0,0,1]
    * right = [0,1,0]
    * straight = [1,0,0]

