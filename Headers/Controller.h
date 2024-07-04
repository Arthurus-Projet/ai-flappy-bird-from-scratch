#ifndef COLLISION_H
#define COLLISION_H

#include "Player.h"

class Controller {
public:
    Player player;

public:
	Controller();

	Controller(Player player);

	std::pair<double, double> positionWallToPlayer(double rayon, int **map);
	double playerInTheFieldOfVision(double hyp, double posSoliderX, double posSoliderY);
	double angleToEnemy(double hyp, double posSoliderX, double posSoliderY, int **map);

    std::pair<double, double> controller_0_90(int** map, double angle) const;
	std::pair<double, double> controller_90_180(int** map, double angle) const;
	std::pair<double, double> controller_270_360(int** map, double angle) const;
	std::pair<double, double> controller_180_270(int** map, double angle) const;
};

#endif 

