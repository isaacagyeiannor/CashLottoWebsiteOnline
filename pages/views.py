from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()
# class PagesView(LoginRequiredMixin, TemplateView):
class PagesView(TemplateView):
    pass

#  Authentication

pages_authentication_login_view = PagesView.as_view(
    template_name="pages/authentication/auth-login.html"
)

pages_authentication_register_view = PagesView.as_view(
    template_name="pages/authentication/auth-register.html"
)
pages_authentication_recoverpw_view = PagesView.as_view(
    template_name="pages/authentication/auth-recoverpw.html"
)
pages_authentication_lockscreen_view = PagesView.as_view(
    template_name="pages/authentication/auth-lock-screen.html"
)
pages_authentication_logout_view = PagesView.as_view(
    template_name="pages/authentication/auth-logout.html"
)
pages_authentication_confirm_mail_view = PagesView.as_view(
    template_name="pages/authentication/auth-confirm-mail.html"
)
pages_authentication_email_verification_view = PagesView.as_view(
    template_name="pages/authentication/auth-email-verification.html"
)
pages_authentication_two_step_verification_view = PagesView.as_view(
    template_name="pages/authentication/auth-two-step-verification.html"
)
#  Pages
pages_starter_page_view = PagesView.as_view(template_name="pages/pages-starter.html")
pages_maintenance_view = PagesView.as_view(template_name="pages/pages-maintenance.html")
pages_comingsoon_view = PagesView.as_view(template_name="pages/pages-comingsoon.html")
pages_timeline_view = PagesView.as_view(template_name="pages/pages-timeline.html")
pages_faqs_view = PagesView.as_view(template_name="pages/pages-faqs.html")
pages_pricing_view = PagesView.as_view(template_name="pages/pages-pricing.html")
pages_error_404_view = PagesView.as_view(template_name="pages/pages-404.html")
pages_error_500_view = PagesView.as_view(template_name="pages/pages-500.html")

#Blog

pages_blogs_view = PagesView.as_view(template_name="pages/blogs.html")
pages_create_blog_view = PagesView.as_view(template_name="pages/create-blog.html")
pages_delete_blog_view = PagesView.as_view(template_name="pages/delete-blog.html")
pages_view_blog_view = PagesView.as_view(template_name="pages/view-blog.html")
pages_testimonials_view = PagesView.as_view(template_name="pages/testimonials.html")
pages_create_testimonial_view = PagesView.as_view(template_name="pages/create-testimonial.html")
pages_view_testimonial_view = PagesView.as_view(template_name="pages/view-testimonial.html")
pages_delete_testimonial_view = PagesView.as_view(template_name="pages/delete-testimonial.html")
pages_add_draw_view = PagesView.as_view(template_name="pages/add-draw.html")
pages_all_draws_view = PagesView.as_view(template_name="pages/all-draws.html")
pages_all_draw_form_view = PagesView.as_view(template_name="pages/all-draw-form.html")
pages_all_draw_edit_view = PagesView.as_view(template_name="pages/all-draw-form.html")
pages_all_draw_delete_view = PagesView.as_view(template_name="pages/all-draw-delete.html")
pages_add_win_draw_view = PagesView.as_view(template_name="pages/add-win-draw.html")


# Karlo Added Web Pages

#Blog
# class BlogList(ListView):
#     model = Blog
#     paginate_by=4
# pages_blogs_view = BlogList.as_view(template_name="pages/blogs.html")


# class CreateBlogListView(CreateView): 
#     form_class = BlogForm
#     context_object_name ='form' 
#     success_url = '/pages/blogs'
# pages_create_blog_view =CreateBlogListView.as_view(template_name="pages/create-blog.html")

# class DeleteViewBlog(DeleteView): 
#     model = Blog
#     context_object_name ='delete' 
#     success_url = '/pages/blogs'
# pages_delete_blog_view =DeleteViewBlog.as_view(template_name="pages/delete-blog.html")

# class BlogDetailView(DetailView): 
#     model = Blog
#     context_object_name ='detail' 
#     success_url = '/pages/blogs'
# pages_view_blog_view =BlogDetailView.as_view(template_name="pages/view-blog.html")


# #Testimonials
# class TestimonialsList(ListView):
#     model = Testimonial
#     paginate_by=4
# pages_testimonials_view = TestimonialsList.as_view(template_name="pages/testimonials.html")

# class CreateTestimonials(CreateView): 
#     form_class = TestimonialForm
#     context_object_name ='form' 
#     success_url = '/pages/blogs'
# pages_create_testimonial_view = CreateTestimonials.as_view(template_name="pages/create-testimonial.html")


# class TestimonialsDetailView(DetailView): 
#     model = Testimonial
#     context_object_name ='detail' 
#     success_url = '/pages/blogs'
# pages_view_testimonial_view = TestimonialsDetailView.as_view(template_name="pages/view-testimonial.html")

# class DeleteTestimonials(DeleteView): 
#     model = Testimonial
#     context_object_name ='delete' 
#     success_url = '/pages/blogs'
# pages_delete_testimonial_view = DeleteTestimonials.as_view(template_name="pages/delete-testimonial.html")

# #Draw
# class CreateAddDraw(CreateView): 
#     form_class = AddDrawForm
#     context_object_name ='form' 
#     success_url = '/pages/blogs'
# pages_add_draw_view =CreateAddDraw.as_view(template_name="pages/add-draw.html")

# class AllDrawList(ListView):
#     model = AllDraw
#     context_object_name ='page_obj' 
# pages_all_draws_view = AllDrawList.as_view(template_name="pages/all-draws.html")

# class CreateAllDraw(CreateView): 
#     form_class = AllDrawForm
#     context_object_name ='form' 
#     success_url = '/pages/blogs'
# pages_all_draw_form_view = CreateAllDraw.as_view(template_name="pages/all-draw-form.html")

# class AllDrawEdit(UpdateView): 
#     model =  AllDraw
#     form_class = AllDrawForm
#     context_object_name ='form' 
#     success_url = '/pages/blogs'
# pages_all_draw_edit_view = AllDrawEdit.as_view(template_name="pages/all-draw-form.html")

# class AllDrawDelete(DeleteView): 
#     model =  AllDraw
#     context_object_name ='delete' 
#     success_url = '/pages/blogs'
# pages_all_draw_delete_view = AllDrawDelete.as_view(template_name="pages/all-draw-delete.html")

# class CreateAddWinDraw(CreateView): 
#     form_class =AddWinDrawForm
#     context_object_name ='form' 
#     success_url = '/pages/blogs'
# pages_add_win_draw_view = CreateAddWinDraw.as_view(template_name="pages/add-win-draw.html")




#Users
pages_all_users_view = PagesView.as_view(template_name="pages/all-users.html")
pages_all_forecasters_view = PagesView.as_view(template_name="pages/all-forecasters.html")
pages_merchants_view = PagesView.as_view(template_name="pages/merchants.html")

#Bankers
pages_bankers_view = PagesView.as_view(template_name="pages/bankers.html")
pages_banker_view= PagesView.as_view(template_name="pages/add-banker.html")
pages_banker_stats_view = PagesView.as_view(template_name="pages/banker-stats.html")

#Forecasters
pages_number_verification_view = PagesView.as_view(template_name="pages/number-verification.html")

#All Stakes
pages_all_user_stakes_view = PagesView.as_view(template_name="pages/all-user-stakes.html")
pages_add_merchant_stake_view = PagesView.as_view(template_name="pages/add-merchant-stake.html")
pages_all_merchant_stake_view = PagesView.as_view(template_name="pages/all-merchant-stake.html")

#Account
pages_deposit_credit_view = PagesView.as_view(template_name="pages/deposit-credit.html")
pages_local_withdraw_view = PagesView.as_view(template_name="pages/local-withdrawals.html")
pages_bank_withdraw_view = PagesView.as_view(template_name="pages/bank-withdrawals.html")
pages_commissions_view = PagesView.as_view(template_name="pages/commissions.html")
pages_latest_transactions_view = PagesView.as_view(template_name="pages/latest-transactions.html")
pages_win_audits_view = PagesView.as_view(template_name="pages/win-audits.html")
pages_win_audit_fail_view = PagesView.as_view(template_name="pages/win-audit-fail.html")
pages_all_subscriptions_view = PagesView.as_view(template_name="pages/all-subscriptions.html")
pages_account_summary_view = PagesView.as_view(template_name="pages/account-summary.html")
pages_account_services_view = PagesView.as_view(template_name="pages/account-services.html")

# pages_add_merchant_stake_view = PagesView.as_view(template_name="pages/add-merchant-stake.html")
# pages_all_merchant_stake_view = PagesView.as_view(template_name="pages/all-merchant-stake.html")

#Admin
pages_users_view = PagesView.as_view(template_name="pages/user-view.html")
pages_add_user_view = PagesView.as_view(template_name="pages/add-user.html")

#Add Ons
pages_add_recent_stakes_view = PagesView.as_view(template_name="pages/add-recent-stakes.html")
pages_add_recent_wins_view = PagesView.as_view(template_name="pages/add-recent-wins.html")

# Horizontal
pages_horizontal_layout_view = PagesView.as_view(
    template_name="pages/horizontal/layouts-horizontal.html"
)












