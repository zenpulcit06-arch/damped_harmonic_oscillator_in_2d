/*file name simulation */
#include <stdio.h>

int main()
{
  double x,y,vx,vy,ax,ay,kx,ky,m,Ex,Ey,E,dt,T,bx,by,t=0;
  int steps;

  FILE *var = fopen("data.csv","w");
  FILE *cons = fopen("const.csv","w");

  if (var == NULL){
    printf("Error opening data.csv\n");
    return 1;
  }
 if (cons == NULL){
    printf("Error opening cons.csv\n");
    return 1;
  }

  printf("Enter mass of particle\n");
  scanf("%lf",&m);

  printf("Enter intial particle cordinate\n");
  scanf("%lf %lf",&x,&y);

  printf("Enter intial velocity cordinate\n");
  scanf("%lf %lf",&vx,&vy);

  printf("Enter Restoring force constant in terms of cordinate\n");
  scanf("%lf %lf",&kx,&ky);

  printf("Enter damping force constant in terms of cordinate\n");
  scanf("%lf %lf",&bx,&by);

  printf("Enter simulation time\n");
  scanf("%lf",&T);

  printf("Enter time step length\n");
  scanf("%lf",&dt);

  if(dt <= 0 || T<= 0 || m<= 0 || kx <=0 || ky <= 0 ) {
    printf("Invalid parameters\n");
    return 1;
  }

  fprintf(var, "t,x,y,vx,vy,ax,ay,Ex,Ey,E\n");
  fprintf(cons, "m,bx,by,kx,ky\n");
  fprintf(cons, "%lf,%lf,%lf,%lf,%lf\n",m,bx,by,kx,ky);
  fclose(cons);
  ax = (-kx*x-bx*vx)/m;
  ay = (-ky*y-by*vy)/m;

  steps = (int)(T/dt);

  for (int i = 0;i<=steps;i++) {
    Ex = 0.5*kx*x*x + 0.5*m*vx*vx;
    Ey = 0.5*ky*y*y + 0.5*m*vy*vy;
    E = Ex + Ey;
    fprintf(var, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf\n",t,x,y,vx,vy,ax,ay,Ex,Ey,E);
    vx += ax*dt;
    vy += ay*dt;
    x += vx*dt;
    y += vy*dt;
    ax =( -kx*x-bx*vx)/m;
    ay =( -ky*y-by*vy)/m;
    t = t +dt;
  }
fclose(var);
  return 0;
}
