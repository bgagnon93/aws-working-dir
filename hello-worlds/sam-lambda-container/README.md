## Lambda Container

Deployment of the containers is tricky, because I wish to re-use the same tag as I go through my development iterations. To this end, I have created a bash script that uses Docker the project and push it to ECR, and uses sam to orchestrate deployment. I can just run this script whenever I wish to deploy changes in the template:

```
. deploy.bash
```

This function comes with an API. It's a simple hard-coded GET, so I can just navigate to the below url to see it working:

## Architecture

<img src="https://user-images.githubusercontent.com/38666646/187336795-dffd24ef-89e8-46a0-b8eb-e96126efa1e0.png" alt="training-app-architecture" width="500">