## Data Scraping
**Github API**  was used to fetch the data. Endpoint **get** */search/users* with query params as *location:Bangalore and followers>100* was used to fetch the list of users who live in *Bangalore* and have more than 100 followers. Endpoint **get** */users/{username}*  is used to fetch the details of said users. And finally the last endpoint used was **get** */users/{username}/repos* to fetch public repositories of the users with limiting the maximum number of repositories to most recently pushed 500 with pagination as github limits the maximum number of items per request to 100. Rate limiter *time.sleep()* was used to avoid the rate limit set by github.

## Data Analysis
After analyzing the data it can be seen that there are more than 49,000 repositories being managed by almost 600 users. 
**Most repositories by a single user:** The user with the most repositories in the data is *manjunath5496*, with more than 1500 public repositories. 
**Most popular user:** *krishnaik06* is the most followed user with almost 31,000 followers.
**Most popular repository:** The most popular repository with more than 48,000 stargazers is *Hack-with-Github/Awesome-Hacking* by *Hack-with-Github*.

## Action Recommended for Developers
Taking a look at the most stargazed repository *Hack-with-Github/Awesome-Hacking*, it can indicate that there is more interest in the curated content. Developers can create more repositories with topics that are more trending like AI, cybersecurity, etc.

Looking at the most followed user *krishnaik06*, it can be seen that developers with expertise in widely applicable field such as **Data Science** draw more attention. For developers looking gain more attention can try to engage in more user engagement content like quiz, guides and demo projects. Developers can consider sharing their knowledge with beginners by creating road maps to navigate in the tech space.

On looking at the programming languages used in the data, there are more than 160 unique languages used which strongly indicate the diversity in tech stacks. However it can also infer that gaining expertise in more niche languages can make developers more stand out from the crowd diversifying their portfolio and making them more hireable.