# 0422 django

```python
# prefetch
def detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User.objects.annotate(
                            followers_count=Count('followers'),
                                followings_count=Count('followings')
                                ), pk=user_pk)
    followings = user.followings.prefetch_related(
                                            Prefetch('score_set',
                                            queryset=Score.objects.select_related('movie').order_by('-value'),
                                            to_attr='score_set_value_order'
                                            ))
    context = {'user_info': user, 'followings': followings}
    return render(request, 'accounts/detail.html', context)
```





```python
# annotate
def detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User.objects.annotate(
                                followers_count=Count('followers'),
                                followings_count=Count('followings')
                                ), pk=user_pk)
    followings = user.followings.prefetch_related(
                                            Prefetch('score_set'),
                                            query_set=Score.objects.select_related('movie').order_by('-value'),
                                            to_attr='score_set_value_order'
                                            )
    context = {'user_info': user, 'followings': followings}
    return render(request, 'accounts/detail.html', context)
```



annotate 컬럼을 추가해서 값을 넣어놓는 것.

prefetch_ralated : 1:N/M:N -> N개를 미리 가져올 때(JOIN table)

select_related : 1:N -> 1개를 미리 가져올 때(JOIN)



### 카카오

REST API 키 : **843ae1ca70e7ff070870cccc6a6b8cf5**

`고급` 의 `코드` : Ccss6qZCSEfkWdiura0A8OiFsY4PLybO