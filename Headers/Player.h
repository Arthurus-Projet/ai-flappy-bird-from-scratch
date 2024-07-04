#ifndef PLAYER_H
#define PLAYER_H

class Player {
private:
    double x;
    double y;
    double speed;
    double angle;
    int health;

public:
    Player();

    Player(double x, double y, double speed, double angle, int health);

    double getX() const;
    double getY() const;
    double getSpeed() const;
    double getAngle() const;
    int getHealth() const;

    void setX(double newX);
    void setY(double newY);
    void setSpeed(double newSpeed);
    void setAngle(double newAngle);
    void setHealth(int newHealth);
};

#endif
