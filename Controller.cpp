#include <iostream>
#include <utility>
#include <cmath>
#include "Headers/MathFunctions.h"
#include "Headers/Controller.h"
#include "Headers/Player.h"


Controller::Controller() {
    // Initialisation par défaut ou vide
}

Controller::Controller(Player player)
    : player(player) {}


std::pair<double, double> Controller::positionWallToPlayer(double rayon, int** map) {
    if (0.0 <= rayon == true && rayon < 90.0 == true) 
        return controller_0_90(map, rayon);

    if (90 <= rayon == true && rayon < 180 == true) 
        return controller_90_180(map, rayon);

    if (270 < rayon == true && rayon < 360 == true) 
        return controller_270_360(map, rayon); 

    return controller_180_270(map, rayon);   
}

double Controller::playerInTheFieldOfVision(double hyp, double posSoliderX, double posSoliderY) {
    for (int rayon = player.getAngle() + 50; rayon >= player.getAngle() - 30; rayon--) {
        int newRayon = modulo(rayon, 360);

        double pos_y = player.getY() - hyp * std::sin(degToRad(newRayon));
        double pos_x = player.getX() + hyp * std::cos(degToRad(newRayon));
        
        if (std::abs(pos_x - posSoliderX) < 0.1 && std::abs(pos_y - posSoliderY) < 0.1)
            return rayon;
        }
    return 100;
    }

double Controller::angleToEnemy(double hyp, double posSoliderX, double posSoliderY, int** map) {
    double rayon = playerInTheFieldOfVision(hyp, posSoliderX, posSoliderY);
    if (rayon != 100) {
        std::pair<double, double> pos = positionWallToPlayer(rayon, map);
        double hypWallPlayer = std::sqrt(std::abs(std::pow(std::abs(player.getX() - pos.first), 2) - std::pow(std::abs(player.getY() - pos.second), 2)));
        //std::cout << controller.player.getX() << " " << controller.player.getY() << std::endl;
        //std::cout << pos.first << " "<< pos.second << " " << hypWallPlayer << " " << hyp << std::endl;
        if (hypWallPlayer > hyp)
            return player.getAngle() - rayon;
        }
    return 400.;
    }


std::pair<double, double> Controller::controller_0_90(int** map, double angle) const {
    double x = player.getX();
    double y = player.getY();

    // Horizontal wall
    double adj = modulo(y, 1.0); // Keeps only the decimal part
    double opp = adj * std::tan(degToRad(90.0 - angle));

    // vertical wall
    double adj2 = 1.0 - modulo(x, 1.0);
    double opp2 = std::tan(degToRad(angle)) * adj2;

    int x_test = std::floor(x + opp);
    int y_test = round(y - adj) - 1;

    bool bool_horizontal = false;
    bool bool_vertical = false;

    std::pair<double, double> return_1;
    std::pair<double, double> return_2;

    if (y_test >= 0 && x_test >= 0) {
        try {
            // We test the first horizontal wall
            if (map[y_test][x_test] != 0) {
                double x_return = (x + opp);
                double y_return = (y - adj);
                return_1 = std::make_pair(x_return, y_return);
                bool_horizontal = true;
            }
        } catch (...) {
        }
    }

    x_test = round(x + adj2);
    y_test = std::floor(y - opp2);

    try{
        // We check the first vertical wall
        if (y_test >= 0 && x_test >= 0) {
            if (map[y_test][x_test] != 0) {
                return_2 = std::make_pair(x + adj2, y - opp2);
                bool_vertical = true;
            }
        }
    } catch(...) {
    }

    if (bool_horizontal == true && bool_vertical == true) {
    if (return_1.first < return_2.first)
        return return_1;
    return return_2;
    }


    // We test all horizontal Walls
    double opp_up = std::tan(degToRad(90.0 -angle));
    int index = 1;

    if (!bool_horizontal) {
        while (true) {
            try {
                if (static_cast<int>(round(y - adj - static_cast<double>(index) - 1.0)) >= 0 && static_cast<int>(std::floor(x + opp + opp_up * static_cast<double>(index))) >= 0 && static_cast<int>(round(y - adj - static_cast<double>(index) - 1.0)) <= 12 && static_cast<int>(std::floor(x + opp + opp_up * static_cast<double>(index))) <= 12) {
                    if (map[static_cast<int>(round(y - adj - static_cast<double>(index) - 1.0))][static_cast<int>(std::floor(x + opp + opp_up * static_cast<double>(index)))] != 0) {
                        double return_x = (x + opp + opp_up * static_cast<double>(index));
                        double return_y = (std::floor(y - adj - static_cast<double>(index)));
                        return_1 = std::make_pair(return_x, return_y);
                        break;
                    }
                } else {
                    return_1 = std::make_pair(3000.0, 3000.0);
                    break;
                }
            } catch (...) {
                return_1 = std::make_pair(3000.0, 3000.0);
                break;
            }

            index++;
        }
    }


    // We check all the vertical wall
    double opp_right = std::tan(degToRad(angle));
    index = 1;
    if (!bool_vertical) {
        while (true) {
            int y_ = std::floor(y - opp2 - opp_right * index);
            int x_ = (round(x + adj2) + index);
            try {
                if (y_ >= 0 && x_ >= 0  && y_ <= 12 && x_ <= 12) {
                    if (map[static_cast<int>(y_)][static_cast<int>(x_)] != 0) {
                        double return_x_2 = (x + adj2 + static_cast<double>(index));
                        double return_y_2 = (y - opp2 - opp_right * static_cast<double>(index));
                        return_2 = std::make_pair(return_x_2, return_y_2);
                        break;
                    }
                } else {
                    return_2 = std::make_pair(3000.0, 3000.0);
                    break;
                }
            } catch (...) {

                return_2 = std::make_pair(3000.0, 3000.0);
                break;
            }
            index++;
        }
    }

    if (return_1.first == 3000.0)
      return return_2;
    if (return_2.first == 3000.0)
      return return_1;
    if (return_1.first < return_2.first)
      return return_1;
    else
      return return_2;
    }

std::pair<double, double> Controller::controller_90_180(int** map, double angle) const {
    double x = player.getX();
    double y = player.getY();
  
    double vertical_angle = 90.0 - (angle - 90.0);

    // Horizontal wall
    double adj = modulo(y, 1);
    double opp = adj * std::tan(degToRad(90.0 -angle));

    // vertical wall
    double adj2 = modulo(x, 1);
    double opp2 = std::tan(degToRad(vertical_angle)) * adj2;


    int x_test =std::floor(x + opp);
    int y_test = round_(y - adj) - 1;

    bool bool_horizontal = false;
    bool bool_vertical = false;

    std::pair<double, double> return_1;
    std::pair<double, double> return_2;

    try {
        // We test the first horizontal wall
        if (map[y_test][x_test] != 0) {
            return_1 = std::make_pair(x + opp, y - adj);
            bool_horizontal = true;
        }
    } catch(...) {
    }


    x_test = round_(x - adj2);
    y_test = std::floor(y - opp2);

    try {
        // We check the first vertical wall
        if (y_test >= 0 && x_test - 1 >= 0)  {
            if (map[y_test][x_test - 1] != 0) {
                return_2 = std::make_pair(x - adj2, y - opp2);
                bool_vertical = true;
            }
        }
    } catch(...) {
    }


    if (bool_horizontal && bool_vertical) {
        if (return_1.first > return_2.first)
            return return_1;
        return return_2;
        }


    // We test all horizontal Walls
    double opp_up = std::tan(degToRad(90 - angle));
    int index = 1;

    if (bool_horizontal == false) {
        while (true) {
            try {
                long x_ = static_cast<long>(round_(y - adj -index - 1));
                long y_ = static_cast<long>(std::floor(x + opp + opp_up * index));
                if (y_ >= 0 && x_ >= 0 && y_ <= 12 && x_ <= 12)
                {
                    if (map[x_][y_] != 0) {
                    return_1 = std::make_pair(x + opp + opp_up * index, std::floor(y - adj -index));
                    break;
                    }
                } else {
                    return_1 = std::make_pair(3000.0, 3000.0);
                    break;
                }
            } catch(...) {
                return_1 = std::make_pair(3000.0, 3000.0);
                break;
            }
            index++;
        }
    }

    // We check all the vertical wall
    double opp_right = std::tan(degToRad(vertical_angle));
    index = 1;
    if (!bool_vertical){
        while (true) {
            int y_ = std::floor(y - opp2 -opp_right * index);
            int x_ = round_(x - adj2) - index;
            try {
                if (y_ >= 0 && x_ -1 >= 0 && y_ <= 12 && x_ <= 12) {
                    if (map[y_ ][x_ - 1] != 0) {
                        return_2 = std::make_pair(x - adj2 - static_cast<double>(index), y - opp2 - opp_right * static_cast<double>(index));
                        break;
                    }
                } else {
                    return_2 = std::make_pair(3000.0, 3000.0);
                    break;
                }
            } catch(...) {
                return_2 = std::make_pair(3000.0, 3000.0);
                break;
                }
            index++;
        }
    }

      if (return_1.first == 3000.0)
        return return_2;
      if (return_2.first == 3000.0)
        return return_1;
      if (return_1.first > return_2.first)
        return return_1;
      else
        return return_2;
    }



std::pair<double, double> Controller::controller_270_360(int** map, double angle) const {

    double x = player.getX();
    double y = player.getY();

    double vertical_angle = 90.0 - modulo(angle, 90.0);
    double horizontal_angle = modulo(angle, 270);

    // Horizontal wall
    double adj = 1 - modulo(y, 1);
    double opp = adj * std::tan(degToRad(horizontal_angle));

    // vertical wall
    double adj2 = 1.0 - modulo(x, 1);
    double opp2 = std::tan(degToRad(vertical_angle)) * adj2;


    int x_test = std::floor(x + opp);
    int y_test = round_(y + adj);

    bool bool_horizontal = false;
    bool bool_vertical = false;

    std::pair<double, double> return_1;
    std::pair<double, double> return_2;

    try {
        // We test the first horizontal wall
        if (y_test >= 0 && x_test >= 0) {
            if (map[y_test][x_test] != 0) {
                return_1 = std::make_pair(x + opp, y + adj);
                bool_horizontal = true;
            }
        }
    } catch(...) {
    }


    x_test = round_(x + adj2);
    y_test = std::floor(y + opp2);

    try {
        // We check the first vertical wall
        if (y_test >= 0 && x_test >= 0 && y_test <= 12 && x_test <= 12) {
            if (map[y_test][x_test] != 0) {
                return_2 = std::make_pair(x + adj2, y + opp2);
                bool_vertical = true;
            }
        }
    } catch(...) {
    }


    if (bool_horizontal && bool_vertical) {
        if (return_1.first < return_2.first)
            return return_1;
        return return_2;
    }


    // We test all horizontal Walls
    double opp_up = std::tan(degToRad(horizontal_angle));
    int index = 1;

    if (bool_horizontal == false) {
        while (true) {
            try {
                if (round_(y + adj + index) >= 0 && round_(y + adj + index) <= 12 && std::floor(x + opp + opp_up * index) >= 0 && std::floor(x + opp + opp_up * index) <= 12) {
                    if (map[static_cast<int>(round_(y + adj + index))][static_cast<int>(std::floor(x + opp + opp_up * index))] != 0) {
                        return_1 = std::make_pair(x + opp + opp_up * index, std::floor(y + adj + index));
                        break;
                    }
                } else {
                    return_1 = std::make_pair(3000.0, 3000.0);
                break;
                }
            } catch(...) {
                return_1 = std::make_pair(3000.0, 3000.0);
                break;
            }
            index++;
        }
    }

    // We check all the vertical wall
    double opp_right = std::tan(degToRad(vertical_angle));
    index = 1;
    if (!bool_vertical){
        while (true) {
            int y_ = std::floor(y + opp2 + opp_right * index);
            int x_ = round_(x + adj2) + index;
            try {
                if (y_ >= 0 && x_ >= 0 && y_ <= 12 && x_ <= 12) {
                    if (map[y_ ][x_] != 0) {
                        return_2 = std::make_pair(x + adj2 + static_cast<double>(index), y + opp2 + opp_right * static_cast<double>(index));
                        break;
                    }
            } else {
                return_2 = std::make_pair(3000.0, 3000.0);
                break;
            }
            } catch(...) {
                return_2 = std::make_pair(3000.0, 3000.0);
                break;
            }
            index++;
        }
    }

      if (return_1.first == 3000.0)
        return return_2;
      if (return_2.first == 3000.0)
        return return_1;
      if (return_1.first < return_2.first)
        return return_1;
      else
        return return_2;
    }

std::pair<double, double> Controller::controller_180_270(int** map, double angle) const {
    double x = player.getX();
    double y = player.getY();
    
    double vertical_angle = modulo(angle, 180.0);
    double horizontal_angle = 90.0 - modulo(angle, 180.0);

    // Horizontal wall
    double adj = 1 - modulo(y, 1);
    double opp = adj * std::tan(degToRad(horizontal_angle));

    // vertical wall
    double adj2 = modulo(x, 1);
    double opp2 = std::tan(degToRad(vertical_angle)) * adj2;


    int x_test = std::floor(x - opp);
    int y_test = round_(y + adj);

    bool bool_horizontal = false;
    bool bool_vertical = false;

    std::pair<double, double> return_1;
    std::pair<double, double> return_2;

    try {
        // We test the first horizontal wall
        if (y_test >= 0 && x_test >=0) {
            if (map[y_test][x_test] != 0) {
                return_1 = std::make_pair(x - opp, y + adj);
                bool_horizontal = true;
            }
        }
    } catch(...) {
    }


    x_test = round_(x - adj2);
    y_test = std::floor(y + opp2);

    try {
        // We check the first vertical wall
        if (y_test >= 0 && x_test >= 0 && y_test <= 12 && x_test - 1 <= 12) {
            if (map[y_test][x_test - 1] != 0) {
                return_2 = std::make_pair(x - adj2, y + opp2);
                bool_vertical = true;
            }
        }
    } catch(...) {
    }


    if (bool_horizontal && bool_vertical) {
        if (return_1.first > return_2.first)
            return return_1;
        return return_2;
    }


    // We test all horizontal Walls
    double opp_up = std::tan(degToRad(horizontal_angle));
    int index = 1;

    if (bool_horizontal == false) {
        while (true) {
            try {
                if (round_(y + adj + index) >= 0 && std::floor(x - opp - opp_up * index) >= 0 && round_(y + adj + index) <= 12 && std::floor(x - opp - opp_up * index) <= 12) {
                    if (map[static_cast<int>(round_(y + adj + index))][static_cast<int>(std::floor(x - opp - opp_up * index))] != 0) {
                        return_1 = std::make_pair(x - opp - opp_up * index, std::floor(y + adj + index));
                        break;
                    }
                } else {
                    return_1 = std::make_pair(3000.0, 3000.0);
                    break;
                }
            } catch(...) {
                return_1 = std::make_pair(3000.0, 3000.0);
                break;
            }
            index++;
        }
    }

    // We check all the vertical wall
    double opp_right = std::tan(degToRad(vertical_angle));
    index = 1;
    if (!bool_vertical) {
        while (true) {
            int y_ = std::floor(y + opp2 + opp_right * index);
            int x_ = round_(x - adj2) - index;
            try {
                if (y_ >= 0 && x_ -1 >= 0 && y_ <= 12 && x_ -1 <= 12) {
                    if (map[y_ ][x_ - 1] != 0) {
                        return_2 = std::make_pair(x - adj2 - static_cast<double>(index), y + opp2 + opp_right * static_cast<double>(index));
                        break;
                    }
                } else {
                    return_2 = std::make_pair(3000.0, 3000.0);
                    break;
                }
            } catch(...) {

                return_2 = std::make_pair(3000.0, 3000.0);
                break;
            }
            index++;
        }
    }

      if (return_1.first == 3000.0)
        return return_2;
      if (return_2.first == 3000.0)
        return return_1;
      if (return_1.first > return_2.first)
        return return_1;
      else
        return return_2;
    }

