# 0510

### git branch

- git branch 브랜치명
- git checkout 브랜치명

- 두 개를 합친 브랜치 만들면서 이동은 체크아웃만 쓰면 됨

  -> git checkout -b 브랜치명



> git checkout -b yoon (yoon이라는 branch 를 새로 파고 이동)
>
> touch signup.txt 로 아무 파일이나 만들고 add, commit 후
>
> `git checkout master` 로 마스터브랜치로 돌아가면 만든게 저절로 사라짐
>
> git diff yoon 을 하면 두 커밋이나 디렉토리의 변경점을 보여준다.
>
> git merge yoon 을 하면 마스터와 병합한다.
>
> git branch 라고 하면 현재 존재하는 마스터와 가지의 종류가 보인다.
>
> git branch -d yoon => branch 를 지운다.
>
> git branch ij  => ij 라는 브랜치 생성
>
> git checkout ij => ij브랜치로 이동
>
> ij 에서 movie.txt 만들고 커밋후 master 로 온 후 master 에서 profile.txt 만들고 커밋
>
> 그 후 git merge ij 하면 둘이 병합 그 후 git log 를 띄우면 시간최신순으로 나열됨.

* 같은 파일을 수정해서 병합이 바로 안되는 경우

> 마스터와 브랜치에서 같은 txt 파일의 내용을 수정 add commit 후에 마스터로 돌아와
>
> git merge 브랜치명 을 해주면 
>
> `Auto-merging profile.txt                                                        
> CONFLICT (content): Merge conflict in profile.txt                               
> Automatic merge failed; fix conflicts and then commit the result.               `
>
> 충돌이 일어났으므로 너가 알아서 수정하고 알아서 병합해라..
>
> 문제의 txt 파일을 열어보면 충돌되기 전의 내용 2개를 보여주므로 거기서 선택할 수 있다.
>
> git status 를 쳐도 병합해야한다고 경고가 뜰 것
>
> 그 후 수정을 입맛에 맞게 한 후 (안해도 상관x) git add , commit 하면 정상적으로 된다.

* 다른 경우

> git checkout jeong
>
> git checkout master ( 아직 7개의 커밋이 앞에있다 뜸)
>
> git branch -d jeong ( 원래 병합되면 원래 jeong 을 날려주는 게 맞다.)
>
> git 용어 중 rebase 라고 있는데 commit 이력을 합쳐버리기 때문에 절대 함부로 쓰지 말자!

* github pull request

> github 에서 병합을 할 때 branch에서 master 에게 pull request 를 보내서 
>
> master 가 마음에 들면 병합을 할 수 있다. 병합의 과정도 커밋처럼 기록이 남는다.

