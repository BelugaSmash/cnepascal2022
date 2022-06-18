#define RECTSIZE 10

double g;
bool pressed, down, up, waiting;
int px, py;
int score;

struct RECT {
  int left, right, top, bottom;
};

bool collide(int x, int y, int w, int h, int _x, int _y, int _w, int _h) {
  RECT a, b;
  a.left = x, a.right = x + w;
  a.top = y, a.bottom = y + h;
  
  b.left = _x, b.right = _x + _w;
  b.top = _y, b.bottom = _y + _h;

  return a.left < b.right && a.top < b.bottom && a.right > b.left && a.bottom > b.top;
}

void input() {
  digitalWrite(13, HIGH);
  TSPoint p = ts.getPoint();
  digitalWrite(13, LOW);
  if (p.z > MINPRESSURE && p.z < MAXPRESSURE) {
    if (!pressed) {
      down = true;
    }
    else {
      down = false;
    }
    pressed = true;
    up = false;
  }
  else {
    up = true;
    pressed = false;
    down = false;
  }
}

void Init() {
  prevy = gravity = 0;
  y = tft.height() / 2;
  tft.fillScreen(CYAN);
  px = tft.width();
  py = tft.height() / 2 + rand() % 101 - 50;
  score = 0;
}

void setup(void) {
  srand(time(NULL));
  Serial.begin(9600);

  tft.reset();
  tft.begin(37697);
  tft.setRotation(1);

  tft.fillScreen(CYAN);

  Init();

  pinMode(13, OUTPUT);z
  pinMode(22, INPUT);
}

void loop() {
  input();
  pinMode(XM, OUTPUT);
  pinMode(YP, OUTPUT);
  if (!waiting) {
    tft.fillRect(30, prevy - RECTSIZE / 2, RECTSIZE, RECTSIZE, CYAN);
    tft.fillRect(30, y - RECTSIZE / 2, RECTSIZE, RECTSIZE, RED);
    tft.fillRect(px + 5, 0, RECTSIZE, py - 25, CYAN);
    tft.fillRect(px, 0, RECTSIZE, py - 25, GREEN);
    tft.fillRect(px + 5, py + 25, RECTSIZE, tft.height() - py + 25, CYAN);
    tft.fillRect(px, py + 25, RECTSIZE, tft.height() - py + 25, GREEN);
    tft.setTextSize(2); tft.setCursor(30, 30);
    tft.setTextColor(BLACK); tft.print(score);
    if (down || digitalRead(22) == HIGH) gravity = -3.0;
    prevy = y;
    y += gravity;
    gravity += 0.3; 
    px -= 5;
    if (px < -RECTSIZE) {
      px = tft.width();
      py = tft.height() / 2 + rand() % 101 - 50;
      tft.setTextSize(2); tft.setCursor(30, 30);
      tft.setTextColor(CYAN); tft.print(score);
      score++;
    }
    if (0 > y - RECTSIZE / 2 || y + RECTSIZE / 2 >= tft.height() ||
      collide(30, y - RECTSIZE / 2, RECTSIZE, RECTSIZE, px, 0, RECTSIZE, py - 25) ||
      collide(30, y - RECTSIZE / 2, RECTSIZE, RECTSIZE, px, py + 25, RECTSIZE, tft.height() - py + 25)) {
      tft.setTextSize(3); tft.setTextColor(BLACK);
      tft.setCursor(tft.width() / 2 - 90, tft.height() / 2 - 30);
      tft.print("Game Over!\n"); tft.setTextSize(2);
      tft.setCursor(0, tft.height() / 2);
      tft.print("     touch to restart");
      waiting = true;
    }
  }
  else if (down || digitalRead(22) == HIGH) {
    waiting = false;
    Init();
  }
  Serial.println("");
}